# This A E-Mail Slicer
# Taking E-Mail Address From User

print("What Is Your E-Mail Address ?")
E_mail=input("Enter ").strip()

# Distancing User Name From E_Mail
user_name=E_mail[:E_mail.index("@")]

# Distancing Domain Name From E_Mail
domain_name=E_mail[E_mail.index("@")+1:]
output = "Your User Name Is " + user_name +" And Your Domain Name Is "+ domain_name
print(output)