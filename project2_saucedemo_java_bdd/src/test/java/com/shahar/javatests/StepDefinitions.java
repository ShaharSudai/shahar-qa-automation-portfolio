package com.shahar.javatests;

import com.shahar.javatests.pages.*;
import com.shahar.javatests.utils.DriverFactory;
import io.cucumber.java.Before;
import io.cucumber.java.After;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.time.Duration;

public class StepDefinitions {
    private WebDriver driver;

    public static final String SITE = "https://www.saucedemo.com";

    private LoginPage loginPage;
    private ProductsPage productsPage;
    private ProductPage productPage;
    private CartPage cartPage;
    private CheckoutPage checkoutPage;
    private FinalCheckoutPage finalCheckoutPage;
    private OrderCompletionPage orderCompletionPage;

    @Before
    public void setUp() {
        driver = DriverFactory.createDriver(DriverFactory.BrowserType.EDGE);
    }

    @Given("User is on the login page")
    public void user_is_on_login_page() {
        driver.get(SITE);
        loginPage = new LoginPage(driver);
    }

    @When("User enters a username {string} and password {string} and logs in")
    public void user_enters_a_username_and_password_and_logs_in(
            String username, String password) {
        loginPage.login(username, password);
    }

    @Then("User navigates to the inventory page")
    public void user_navigates_to_inventory_page() {
        if (productsPage == null) {
            productsPage = new ProductsPage(driver);
        }
        Assert.assertTrue(productsPage.isPageOpened(), "Login failed!");
    }

    @Given("User navigates to the product page for {string}")
    public void user_navigates_to_the_product_page(String productName) {
        productsPage.navigateToProductPage(productName);

        if (productPage == null) {
            productPage = new ProductPage(driver);
        }
    }

    @When("User adds the product to cart")
    public void user_adds_the_product_to_cart() {
        productPage.addToCart();
    }

    @Then("Button text on the page should change to \"Remove\"")
    public void button_text_on_the_page_should_change_to_remove() {
        // WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        Assert.assertEquals(productPage.getButtonText(), "Remove",
                "Button text did not change");
    }

    @And("User navigates back to the inventory page")
    public void user_navigates_back_to_the_inventory_page() {
        driver.navigate().back();
    }

    @When("User navigates to the cart page")
    public void user_navigates_to_the_cart_page() {
        productsPage.navigateToCart();
        if (cartPage == null) {
            cartPage = new CartPage(driver);
        }
    }

    @Then("User should be on the cart page")
    public void user_should_be_on_the_cart_page() {
        Assert.assertTrue(cartPage.isPageOpened(), "Cart page not loaded");
    }

    @And("The cart should contain product {string}")
    public void the_cart_should_contain_product(String productName) {
        Assert.assertTrue(cartPage.productInCart(productName));
    }

    @And("The cart item count should be {string}")
    public void the_cart_item_count_should_be(String number) {
        Assert.assertEquals(cartPage.getCartItemCount(), number,
                "Incorrect number of items in the cart");
    }

    @And("The checkout button text should be \"Checkout\"")
    public void the_checkout_button_text_should_be_checkout() {
        Assert.assertEquals(cartPage.getContinueButtonText(), "Checkout",
                "Incorrect button text on the cart page");
    }


    @When("User clicks on the checkout button")
    public void user_clicks_on_the_checkout_button() {
        cartPage.continueCheckout();
        if (checkoutPage == null) {
            checkoutPage = new CheckoutPage(driver);
        }
    }

    @Then("User should be on the checkout step one page")
    public void user_should_be_on_the_checkout_step_one_page() {
        Assert.assertTrue(checkoutPage.isPageOpened(), "Checkout page not loaded");
    }

    @When("User enters first name {string}, last name {string}, and zip code {string}")
    public void user_enters_first_name_last_name_and_zip_code(
            String firstName, String lastName, String zipCode
    ) {
        checkoutPage.enterDetails(firstName, lastName, zipCode);
    }

    @Then("The field values should be firstname {string}, lastname {string}, and zip code {string}")
    public void the_field_values_should_be_firstname_lastname_and_zip_code(
            String firstName, String lastName, String zipCode
    ) {
        Assert.assertEquals(checkoutPage.getFirstNameFieldValue(), firstName,
                "First name field value is incorrect");
        Assert.assertEquals(checkoutPage.getLastNameFieldValue(), lastName,
                "Last name field value is incorrect");
        Assert.assertEquals(checkoutPage.getZipCodeFieldValue(), zipCode,
                "Zip code field value is incorrect");
    }


    @When("User clicks on the continue checkout button")
    public void user_clicks_on_the_continue_checkout_button() {
        checkoutPage.continueCheckout();
        if (finalCheckoutPage == null) {
            finalCheckoutPage = new FinalCheckoutPage(driver);
        }
    }

    @Then("User should be on the checkout step two page")
    public void user_should_be_on_the_checkout_step_two_page() {
        Assert.assertTrue(finalCheckoutPage.isPageOpened(),
                "Checkout page not loaded");
    }

    @Then("The payment info should be {string}")
    public void the_payment_info_should_be(String paymentInfo) {
        Assert.assertEquals(finalCheckoutPage.getPaymentInfoValue(), paymentInfo);
    }

    @And("The shipping info should be {string}")
    public void the_shipping_info_should_be(String shippingInfo) {
        Assert.assertEquals(finalCheckoutPage.getShippingInfoValue(), shippingInfo);
    }

    @And("The total should be {string}")
    public void the_total_should_be_(String totalValue) {
        Assert.assertEquals(finalCheckoutPage.getTotalLabel(), totalValue);
    }

    @When("User finishes checking out")
    public void user_finishes_checking_out() {
        finalCheckoutPage.finishCheckout();
        if (orderCompletionPage == null) {
            orderCompletionPage = new OrderCompletionPage(driver);
        }
    }

    @Then("User sees completion message and order completion text")
    public void user_sees_completion_message_and_order_completion_text() {
        Assert.assertEquals(orderCompletionPage.getHeaderText(),
                "Thank you for your order!");
        Assert.assertEquals(orderCompletionPage.getBodyText(),
                "Your order has been dispatched, and will arrive just as fast as the pony can get there!");
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
