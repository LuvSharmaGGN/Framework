from conftest import page


class verticals:
    def __init__(self,page):
        self.page=page;

        #hover for vertical tab
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('(//img[@alt="trading"])[1]')
        self.retail_and_ecommerce=page.locator('(//strong[text()="Retail and Ecommerce"])[1]')
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.fintech_mobile_app_development=page.locator('//strong[text()="Healthcare"]')
        self.custom_App=page.locator('//strong[text()="Custom App"]')
        
        #Trading Sub Menu
        self.Stock_trading=page.locator('(//a[text()="Stock Trading"])[1]')
        self.algo_Trading=page.locator('(//a[text()="Algo Trading"])[1]')
        self.paper_trading=page.locator('(//a[text()="Paper Trading"])[1]')
        self.custom_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_Trading=page.locator('(//a[text()="CFD Trading"])[1]')
        self.webportal_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.stock_trading_development_massachusetts=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.trading_Options=[self.Stock_trading,self.algo_Trading,self.paper_trading,self.custom_trading,self.cfd_Trading,
                              self.webportal_trading,self.stock_trading_development_massachusetts]

        #Retail and Ecommerce
        self.ecommerce_web_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecommerce_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.Retail_Ecommerce_Options=[self.ecommerce_web_development,self.ecommerce_app_development]

        #Healthcare
        self.diet_n_nutrition_app=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health_tracking_app=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.healthcare_Options=[self.diet_n_nutrition_app,self.healthcare]

        #Fintech
        self.pos_software=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.Fintech_Options=[self.pos_software,self.crypto]

        #Custom APPS
        self.desktop_application_development=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm_development_company=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm_application=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel_mobile_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.e_learning_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating_app=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.real_estate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.custom_crm_development=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.custom_App_Options=[self.desktop_application_development,self.crm_development_company,
                                 self.hrm_application,self.erp_app_development,
                                 self.travel_mobile_app_development,self.e_learning_mobile,
                                 self.dating_app,self.real_estate,self.custom_crm_development]

    def trading_options_clicking(self):
        for i in self.trading_Options:
            self.vertical.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Retail_Ecommerce_options_Clicking(self):
        for i in self.Retail_Ecommerce_Options:
            self.vertical.hover()
            self.retail_and_ecommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Healthcare_options_clicking(self):
        for i in self.healthcare_Options:
            self.vertical.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Fintech_options_clicking(self):
        for i in self.healthcare_Options:
            self.vertical.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Custom_options_clicking(self):
        for i in self.custom_App_Options:
            self.vertical.hover()
            self.custom_App.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


