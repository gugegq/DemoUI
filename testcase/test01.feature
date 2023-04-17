@UI @DEX
Feature: DQ-36 Dex Homepage with anonymous user
  As an anonymous user, I want to verify the content of each Store and Catalog in DEX Store homepage, and the submenu for each store.

  Background:
    Given DEX user opens the browser and goes to DEX home page.
    * "DEX user" accepts Cookie policies

  @DQ-36 @RegressionTests @UAT @PROD
  Scenario Outline: DQ-36 Check Homepage and Catalog Content for Each Store - US locale
    ###Check Homepage Content - US locale
    Then "DEX user" check the storeName, storeDesc, storePic and learnMoreBtn of '<StoreName>' in Shop By Store Page
    Then "DEX user" click the 'Learn More' button of '<StoreName>' in Shop By Store Page
    ###Store Homepage, 静态全量遍历扫描
    ###Expected Result
    Then "DEX user" check the catalogName, catalogDesc and learnMoreBtn of catalog '<catalogName>' for '<storeName>' in catalog list Page
    Then DEX user navigates to product list page by hovering mouse on the top menu '<storeName>' and click the submenu '<catalogName>'.
    Then DEX user verify the catalog info in PLP: '<catalogName>'
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
      | PLM Store | NX Cloud Connected Products        |
      | MS Store  | Step 1 Access IoT                  |
      | IEM Store | Manufacturing & Process Industries |
      | ISS Store | Machine Tool Software Store        |
    ###每个Store对应1个Scenario，分别打开each Store的Homepage
    Examples:
      | StoreName                   |
      | PLM Store                   |
      | MindSphere Store            |
      | Industrial Edge Marketplace |
      | Industrial Software Store   |