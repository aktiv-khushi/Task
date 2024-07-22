odoo.define('custom_widget.ColorPickerWidget', function(require) {
    'use strict';
console.log("11111111111111111111111")
    const fieldRegistry = require('web.field_registry_owl');
    const { Field } = require('web.basic_fields');
    const { Component, useState } = owl;

    class ColorPickerWidget extends Field {
        constructor() {
            super(...arguments);
            this.state = useState({ value: this.value });
        }

        _onChange(event) {
            this._setValue(event.target.value);
        }

        get value() {
            return this.state.value;
        }

        set value(val) {
            this.state.value = val;
        }

        render() {
            return this.renderElement();
        }

        renderElement() {
            this.el.innerHTML = `
                <input type="color" value="${this.value}" />
            `;
            this.el.querySelector('input').addEventListener('input', this._onChange.bind(this));
        }
    }

    fieldRegistry.add('color_picker_widget', ColorPickerWidget);
});
