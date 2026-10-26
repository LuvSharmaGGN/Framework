class blog:
    def __init__(self,page):
        #blog categories
        self.page=page

        self.Blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]').click()
        self.appDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.ai=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.contentMKTng=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crmDev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digitalMKTNG=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecomm=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.email=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graphicsDsgn=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.sw_company=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.swDev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.uiUx=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.webDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
                    
        self.blog_category=[self.appDev,self.ai,self.contentMKTng,self.crmDev,self.digitalMKTNG,self.ecomm,self.email,
                                self.graphicsDsgn,self.sw_company,self.swDev,self.uiUx,self.webDev]

    def blog_catergories_clicking(self):
        for i in self.blog_category:
            i.click()
            #self.page.wait_for_load_state("load")
            self.page.go_back()
        
