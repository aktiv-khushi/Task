/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.productDescription = publicWidget.Widget.extend({
    selector: '.o_wsale_products_page',
    events: {
        'click #fetch': '_onClickFetch',
        'click #reset': '_onClickReset',
    },

    _onClickFetch: async function (ev) {
        const option = document.querySelector("#option");
        const html = `<span>${option.value}</span>`;
        this._updateProductDescription(html);
    },

    _onClickReset: async function (ev) {
        this._updateProductDescription('');
    },

    _updateProductDescription: function (html) {
        const productDescriptionElement = document.querySelector(".product_description");
        productDescriptionElement.innerHTML = html;
    }
});

export default publicWidget.registry.productDescription;
