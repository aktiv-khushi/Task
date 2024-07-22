/** @odoo-module **/

import { Component } from "@odoo/owl";
import { useState } from "@odoo/owl";
import { onWillUpdateProps } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class MyComponent extends Component {
    static template = "components.MyComponent";
    setup() {
        const fixed = parseInt(localStorage.getItem("values"), 5) || 0;
        this.state = useState({ value: fixed });
        onWillUpdateProps(() => {
            localStorage.setItem("values", this.state.value);
        });
    }

    increment() {
        this.state.value++;
        localStorage.setItem("values", this.state.value);
    }
}
registry.category("actions").add("new_component", MyComponent);