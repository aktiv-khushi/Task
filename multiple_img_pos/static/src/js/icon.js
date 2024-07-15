/** @odoo-module **/

import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";
import { MultiImagePopup } from "./image_popup"
import { onMounted } from "@odoo/owl";

/**
 * This patch extends the functionality of the ProductCard component to
 * add support for displaying multiple images in a popup.
 */
patch(ProductCard.prototype, {
   /**
     * Setup function to initialize the component and mount the product image functionality.
     */
   async setup(){
       super.setup(...arguments);
       onMounted(this.ProductImage);
   },
     /**
     * Fetch the product's attachment IDs once the component is mounted.
     * This method queries the Odoo backend for the product's attachments.
     */
   async ProductImage(){
       this.product = this.props.productId;
       const data = await this.env.services.orm.searchRead('product.product', [['id', '=', this.product]], ['attachment_ids']);
       this.props.attachmentIds = data[0].attachment_ids;
   },
   /**
     * Handle the click event on the image icon.
     * This method fetches the image data for the product's attachments and displays them in a popup.
     */
   async onClickImageIcon() {
        const imageList = [];
        // Iterate through each attachment ID to fetch the image data.
        for (let i = 0; i < this.props.attachmentIds.length; i++) {
            const image = await this.env.services.orm.searchRead('ir.attachment', [['id', '=', this.props.attachmentIds[i]]], ['datas']);

            if (image.length > 0 && image[0].datas) {
                imageList.push(image[0].datas);
            }
        }
        this.imageList = imageList;
        // Show the MultiImagePopup with the fetched image data.
        await this.env.services.popup.add(MultiImagePopup, {
             product: this.product,
             data: imageList,
        });
   }
});
