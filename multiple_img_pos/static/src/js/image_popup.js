/** @odoo-module */
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { useState, useRef, onMounted } from "@odoo/owl";
/**
 * MultiImagePopup class extends AbstractAwaitablePopup to provide a popup for displaying multiple product images.
 * This popup allows users to navigate through a series of images using next and previous buttons.
 */
export class MultiImagePopup extends AbstractAwaitablePopup {
    static template = "multiple_image_pos.MultiImagePopup";
    /**
     * Setup function to initialize the component's state and references.
     * This method overrides the original setup method of AbstractAwaitablePopup.
     */
    async setup() {
        super.setup();
        this.currentIndex = useState({ index: 0 }); // State to keep track of the current image index
        this.items = this.props.data || [];  // Array of images passed through props
        this.imageRef = useRef("itemDisplay"); //Reference to the image element

        onMounted(() => {
            this.updateImage(); // Update the image source when the component is mounted
        });
    }
     /**
     * Function to handle the event when the previous button is clicked.
     * It updates the currentIndex state to show the previous image.
     */
    slidePrev() {
        if (this.currentIndex.index > 0) {
            this.currentIndex.index -= 1;
        } else {
            this.currentIndex.index = this.items.length - 1; // Wrap around to the last image
        }
        this.updateImage(); // Update the image source
    }
    /**
     * Function to handle the event when the next button is clicked.
     * It updates the currentIndex state to show the next image.
     */
    slideNext() {
        if (this.currentIndex.index < this.items.length - 1) {
            this.currentIndex.index += 1;
        } else {
            this.currentIndex.index = 0; // Wrap around to the first image
        }
        this.updateImage(); // Update the image source
    }
    /**
     * Function to update the image source of the img element based on the current index.
     * This function sets the src attribute of the image element to display the current image.
     */
    async updateImage() {
        const imgElement = this.imageRef.el;
        if (imgElement && this.items.length > 0) {
            imgElement.src = `data:image/jpeg;base64,${this.items[this.currentIndex.index]}`;
        } else {
        }
    }
}


