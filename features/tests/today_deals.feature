# Created by natalia at 10/27/2019

Feature: Today's deal


  Scenario: User can switch the windows and add product the cart
    Given Amazon today deal page
    When Store original windows
    When Click on Open Deals
    When Switch to the new openly window
    When Today deals are shown
    And Click on product name
    And Click on product
    And Add product to cart
    And User can close new window and switch back to original
    And Refresh page
    When Cart has one item in it
    When Verify there is one item