import logging


logger = logging.getLogger(__name__)


_control_chars = b"\n\r\t\f\b"
_printable_ascii = _control_chars + bytes(range(32, 127))
_printable_high_ascii = bytes(range(127, 256))


def get_starting_chunk(filename, length=1024):
    """
    :param filename: File to open and get the first little chunk of.
    :param length: Number of bytes to read, default 1024.
    :returns: Starting chunk of bytes.
    """
    # Ensure we open the file in binary mode
    try:
        with open(filename, "rb") as f:
            chunk = f.read(length)
            return chunk
    except IOError as e:
        print(e)


def is_binary_string(bytes_to_check):
    """
    Uses a simplified version of the Perl detection algorithm,
    based roughly on Eli Bendersky's translation to Python:
    http://eli.thegreenplace.net/2011/10/19/perls-guess-if-file-is-text-or-binary-implemented-in-python/

    This is biased slightly more in favour of deeming files as text
    files than the Perl algorithm, since all ASCII compatible character
    sets are accepted as text, not just utf-8.

    :param bytes_to_check: A chunk of bytes to check.
    :returns: True if appears to be a binary, otherwise False.
    """

    # Empty files are considered text files
    if not bytes_to_check:
        return False

    # Now check for a high percentage of ASCII control characters
    # Binary if control chars are > 30% of the string
    low_chars = bytes_to_check.translate(None, _printable_ascii)
    nontext_ratio1 = float(len(low_chars)) / float(len(bytes_to_check))
    logger.debug("nontext_ratio1: %(nontext_ratio1)r", locals())

    # and check for a low percentage of high ASCII characters:
    # Binary if high ASCII chars are < 5% of the string
    # From: https://en.wikipedia.org/wiki/UTF-8
    # If the bytes are random, the chances of a byte with the high bit set
    # starting a valid UTF-8 character is only 6.64%. The chances of finding 7
    # of these without finding an invalid sequence is actually lower than the
    # chance of the first three bytes randomly being the UTF-8 BOM.

    high_chars = bytes_to_check.translate(None, _printable_high_ascii)
    nontext_ratio2 = float(len(high_chars)) / float(len(bytes_to_check))
    logger.debug("nontext_ratio2: %(nontext_ratio2)r", locals())

    if nontext_ratio1 > 0.90 and nontext_ratio2 > 0.90:
        return True

    is_likely_binary = (nontext_ratio1 > 0.3 and nontext_ratio2 < 0.05) or (
        nontext_ratio1 > 0.8 and nontext_ratio2 > 0.8
    )
    logger.debug("is_likely_binary: %(is_likely_binary)r", locals())

    import chardet
    # then check for binary for possible encoding detection with chardet
    detected_encoding = chardet.detect(bytes_to_check)
    logger.debug("detected_encoding: %(detected_encoding)r", locals())

    # finally use all the check to decide binary or text
    decodable_as_unicode = False
    if detected_encoding["confidence"] > 0.9 and detected_encoding["encoding"] != "ascii":
        try:
            bytes_to_check.decode(encoding=detected_encoding["encoding"])
            decodable_as_unicode = True
            logger.debug("success: decodable_as_unicode: " "%(decodable_as_unicode)r", locals())
        except LookupError:
            logger.debug("failure: could not look up encoding %(encoding)s", detected_encoding)
        except UnicodeDecodeError:
            logger.debug("failure: decodable_as_unicode: " "%(decodable_as_unicode)r", locals())

    if is_likely_binary:
        return not decodable_as_unicode

    if decodable_as_unicode:
        return False

    if b"\x00" in bytes_to_check or b"\xff" in bytes_to_check:
        # Check for NULL bytes last
        logger.debug("has nulls:" + repr(b"\x00" in bytes_to_check))
        return True

    return False


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """
    logger.debug("is_binary: %(filename)r", locals())

    # Check if the starting chunk is a binary string
    chunk = get_starting_chunk(filename)
    return is_binary_string(chunk)
