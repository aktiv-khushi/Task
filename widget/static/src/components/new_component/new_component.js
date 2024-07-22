/** @odoo-module **/

import { Component, useState, onWillUpdateProps} from "@odoo/owl";
import { registry } from "@web/core/registry";

export class NewComponent extends Component {
    static template = "components.NewComponent";
    // Setup
    setup() {
        const initialValue = parseInt(localStorage.getItem("new_component_value"), 10) || 0;
        this.state = useState({ value: initialValue });
        onWillUpdateProps(() => {
            localStorage.setItem("new_component_value", this.state.value);
        });
    }

    // Increment
    increment() {
        if (this.state.value >= 0) {
           var element = document.querySelector('.error_msg');
           element.classList.add('d-none');
        }
        this.state.value++;
        localStorage.setItem("new_component_value", this.state.value);
    }

    // decrement
    decrement() {
        console.log('\n----------this.state.value',this.state.value)
        if (this.state.value > 0) {
            this.state.value--;
            localStorage.setItem("new_component_value", this.state.value);
        }
        else{
           var element = document.querySelector('.error_msg');
           element.classList.remove('d-none');
            }
        }

    //Reset
    reset() {
       this.state.value = 0;
    }
}
registry.category("actions").add("new_component", NewComponent);