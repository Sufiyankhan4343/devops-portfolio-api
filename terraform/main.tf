resource "azurerm_resource_group" "rg" {
  name     = "rg-devops-portfolio-project"
  location = "East US" # You can change this to your preferred region
}

resource "azurerm_storage_account" "storage" {
  name                     = "stdevopsportfoliouniq" # Must be globally unique and lowercase
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "app_plan" {
  name                = "asp-devops-portfolio"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "Y1" # Free Consumption Plan
}

resource "azurerm_linux_function_app" "function_app" {
  name                       = "func-devops-portfolio-api" # Must be globally unique
  resource_group_name        = azurerm_resource_group.rg.name
  location                   = azurerm_resource_group.rg.location
  service_plan_id            = azurerm_service_plan.app_plan.id
  storage_account_name       = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key

  site_config {
    application_stack {
      python_version = "3.11"
    }
  }
}