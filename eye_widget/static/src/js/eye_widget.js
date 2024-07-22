/** @odoo-module **/
import { registry } from '@web/core/registry';
import { Component, useState } from '@odoo/owl';
import { CharField } from "@web/views/fields/char/char_field"

console.log("\n\n\n\n1111111111111")
class PasswordToggle extends Component {
    setup(){
        super.setup()
        console.log("setup super calllll")
        this.state = useState({ showPassword: false });
    }
    togglePasswordVisibility() {
        console.log("password visible",this.state.showPassword)
        this.state.showPassword =! this.state.showPassword
    }
    get inputType() {
        console.log("i get input type")
        return this.state.showPassword ? 'text' : 'password';
    }
    
}
PasswordToggle.template = "eye_widget.EyeWidget"
PasswordToggle.supportedTypes = ["char"]

export const eyetogglewidget = {
    ...CharField,
    component: PasswordToggle,
};
registry.category('fields').add('password_toggle', eyetogglewidget);
