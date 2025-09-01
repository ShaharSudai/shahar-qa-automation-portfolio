# SauceDemo Automation Project

This project is part of my QA Automation Portfolio.  
It contains automated test scenarios for the [SauceDemo](https://www.saucedemo.com/) website,
written using **Behave (BDD)** and **Python Selenium**.

## Project Structure
- **features/** → Gherkin feature files  
- **steps/** → Step definitions for the features  
- **pages/** → Page Object Model classes  
- **tests/** → Additional utility tests  

## Feature Files
1. **Login.feature** – Scenarios for valid and invalid login  
2. **Logout.feature** – Scenarios for logging out  
3. **Inventory.feature** – Viewing the product inventory (sorting, filtering)  
4. **Cart.feature** – Cart validations (view cart, item count, totals)  
5. **Checkout.feature** – Checkout Step One (user information form)  
6. **CheckoutOverview.feature** – Checkout Step Two (order overview)  
7. **CheckoutComplete.feature** – Order completion and confirmation message  
8. **Navigation.feature** – Side menu navigation (All Items, About, Logout, Reset App State)  
9. **ErrorHandling.feature** – Error messages (invalid login, required fields in checkout)  
10. **UIValidation.feature** – Basic UI checks (logo, buttons, labels, responsiveness)  

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
behave
