class CheckoutLocators:
    country = {'css': '#showroom-list > li'}
    firts_delivery_method = {
        'css': '#showroom-list > li.showroom.selected-item > div > table > tbody > tr:nth-child(1) > td.bpt-radio'}
    second_delivery_method = {
        'css': '#showroom-list > li.showroom.selected-item > div > table > tbody > tr:nth-child(2) > td.bpt-radio'}
    third_delivery_method = {
        'css': '#showroom-list > li.showroom.selected-item > div > table > tbody > tr:nth-child(3) > td.bpt-radio'}
    vipvip_button = {'css': '#opc-sidebar > div.actions-toolbar > div > button'}
    product_name = {'css': 'div.product-item-name-block > strong > a'}
