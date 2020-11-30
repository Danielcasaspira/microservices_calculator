Feature: Bill

Scenario Outline: Get Bill
    Given a <products> to show 
    When Bill show the products
    Then the <total> of products

    Examples: products
    | products          |  total  |
    |   papa,2          |  3000   |     
    |   arroz,3         |  3000   |   
    |   aceite,2        |  6000   | 
    |   panela,1        |  1000   |   
    |   aguacate,4      |  8000   |    
    


