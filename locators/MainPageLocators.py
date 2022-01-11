class MainPageLocators:
    first_product = \
        {'css': 'div.section.section-product.wrapper_product_tabs.container_horizontal_tab_postions.count_product_tab_1 > div > div > ol > div:nth-child(1) > li > div'}
    list_of_products = {'css':'#maincontent > div.columns > div > div:nth-child(4) > div > div > div:nth-child(2) > div.section.section-product.wrapper_product_tabs.container_horizontal_tab_postions.count_product_tab_1 > div > div > ol > div'}
    product = {'css':list_of_products['css'] + ' > li > div'}
