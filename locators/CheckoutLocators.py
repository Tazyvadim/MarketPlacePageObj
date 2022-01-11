class CheckoutLocators:
    country = {'css':'#showroom-list > li'}
    delivery_method = {'css': country['css'] + '.showroom.selected-item#showroom-list > li.showroom.selected-item > div.showroom-details  > table.showroom-item showroom-delivery table-wrapper > tbody > tr'}
