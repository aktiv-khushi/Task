/** @odoo-module **/

import { WebsiteSale } from '@website_sale/js/website_sale';

WebsiteSale.include({
    events: Object.assign({}, WebsiteSale.prototype.events,{
            'click #fetch': '_onClickFetch',
            'click #reset': '_onClickReset',
        },
        _onClickFetch: async function (ev) {
            const option = document.querySelector("#select_option");
            var html = '<span>' + option.value+ '</span>';
            $(".product_description").empty();
            $('.product_description').append(html);
        }

        _onClickReset: async function (ev) {
            $(".product_description").empty();
        },
});
