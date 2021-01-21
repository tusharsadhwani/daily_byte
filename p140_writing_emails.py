"""
Email addresses are made up of local and domain names. For example in
kevin@dailybyte.com, kevin is the local name and dailybye.com is the
domain name. Email addresses may also contain '+' or '.' characters
besides lowercase letters. If there is a '.' in the local name of the
email address it is ignored. Everything after a '+' in the local name is
also ignored. For example ke.vin+abc@dailybyte.com is equivalent to
kevin@dailybyte.com Given a list of email addresses, find the number of
unique addresses.

Ex: Given the following emails...

emails = [
    "test.email+kevin@dailybyte.com",
    "test.e.mail+john.smith@dailybyte.com",
    "testemail+david@daily.byte.com"
], return 2.
"testemail@dailybyte.com" and "testemail@daily.byte.com" are unique
since the first two email addresses in the list are equivalent.
"""


def count_emails(emails: list[str]) -> int:
    """Return number of unique emails"""
    validated_emails = set[str]()

    for email in emails:
        chars: list[str] = []
        found_plus = False
        is_domain = False
        for char in email:
            if char == '@':
                chars.append(char)
                is_domain = True
                continue

            if is_domain:
                chars.append(char)
                continue

            if char == '.' or found_plus:
                continue

            if char == '+':
                found_plus = True
                continue

            chars.append(char)

        validated_email = ''.join(chars)
        validated_emails.add(validated_email)

    return len(validated_emails)


def main() -> None:
    """Main function"""
    emails = [
        "test.email+kevin@dailybyte.com",
        "test.e.mail+john.smith@dailybyte.com",
        "testemail+david@daily.byte.com"
    ]

    print(count_emails(emails))


if __name__ == "__main__":
    main()
