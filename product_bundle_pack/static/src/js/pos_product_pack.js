/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { ProductScreen } from '@point_of_sale/app/screens/product_screen/product_screen';
//import { ProductCard } from "@pos_self_order/app/components/product_card/product_card";

patch(ProductScreen.prototype, {
    setup() {
        super.setup(...arguments);
        console.log("Patch applied successfully");
        const product = this.props.product;
        console.log("product:::",product)
    }

//patch(ProductCard.prototype, {
//    setup() {
//        this._super.apply(this, arguments);
//        console.log("ProductCard setup called");
//        const product = this.props.product;
//        if (product) {
//            console.log("Product: ", product);
//            this.isProductPack = product.is_product_pack;
//        } else {
//            console.log("Product is undefined");
//        }
//    },
});