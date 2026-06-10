email = "rahul.sharma2026@gmail.com"

# 1. Validation: check @ and .
if email.count("@") == 1 and "@" in email:
    
    username, domain_ext = email.split("@")
    
    if "." in domain_ext:
        
        domain, extension = domain_ext.split(".")
        
        # 2. Count digits in username
        digits = 0
        special = 0
        
        for ch in username:
            if ch.isdigit():
                digits += 1
            elif not ch.isalpha():
                special += 1
        
        # Output
        print("Email:", email)
        print("\nUsername:", username)
        print("Domain:", domain)
        print("Extension:", extension)
        
        print("\nDigits Found:", digits)
        print("Special Characters Found:", special)
        
        print("\nEmail Status: Valid")

    else:
        print("Email Status: Invalid (No '.' after @)")
else:
    print("Email Status: Invalid (Incorrect '@' usage)")