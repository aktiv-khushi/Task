odoo.define('survey_form.salary_range', function (require) {
    "use strict";
var core = require('web.core');

//    const core = require('web.core');
    const Widget = require('web.Widget');

    const QWeb = core.qweb;
    const MyWidget = Widget.extend({
        events: {
            'input .range-slider': '_onRangeInput',
        },

        /**
         * @override
         */
        start: function () {
            const self = this;
            this.$('.range-slider').each(function () {
                const $input = $(this);
                const $value = self.$(`#rangeValue${$input.data('index')}`);
                $input.on('input', function () {
                    $value.text($input.val());
                });
            });
            return this._super.apply(this, arguments);
        },

        /**
         * Handle input event on range slider
         *
         * @private
         * @param {Event} ev
         */
        _onRangeInput: function (ev) {
            const $input = $(ev.currentTarget);
            const $value = this.$(`#rangeValue${$input.data('index')}`);
            $value.text($input.val());
        },
    });

    return MyWidget;
});
