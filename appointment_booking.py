import requests

def get_mobile_number():
    mobile_number = input("Enter your mobile number: ")
    return mobile_number

def get_password():
    password = input("Enter your password: ")
    return password

def get_otp():
    otp = input("Enter the OTP sent to your mobile: ")
    return otp

def book_appointment():
    base_url = "https://payment.ivacbd.com"
    
    # Step 1: Enter mobile number
    mobile_number = get_mobile_number()
    mobile_data = {
        "mobile_number": mobile_number
    }
    response = requests.post(f"{base_url}/", data=mobile_data)
    if response.status_code != 200:
        print("Failed to submit mobile number")
        return
    
    # Step 2: Enter password
    password = get_password()
    login_data = {
        "password": password
    }
    response = requests.post(f"{base_url}/login-auth", data=login_data)
    if response.status_code != 200:
        print("Failed to submit password")
        return
    
    # Step 3: Enter OTP
    otp = get_otp()
    otp_data = {
        "otp": otp
    }
    response = requests.post(f"{base_url}/login-otp", data=otp_data)
    if response.status_code != 200:
        print("Failed to submit OTP")
        return
    
    # Step 4: Fill up the form
    form_data = {
        # Add form fields here
    }
    response = requests.post(base_url, data=form_data)
    if response.status_code == 200:
        print("Appointment booked successfully!")
    else:
        print("Failed to book appointment")

if __name__ == "__main__":
    book_appointment()
