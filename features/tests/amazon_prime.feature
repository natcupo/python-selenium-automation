# Created by natala at 10/14/2019
Feature: Test for amazon prime functionality


  Scenario: Amazon Prime page has 8 boxes
    Given Open Amazon Internet page
    When Click on Try Prime
    When Click on try button
    Then Verify 8 boxes are present