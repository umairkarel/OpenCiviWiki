cw = {};
BB = Backbone;

_.templateSettings = {
    evaluate: /\{\{#(.+?)\}\}/g,
    interpolate: /\{\{=(.+?)\}\}/g,
    escape: /\{\{(?!#|=)(.+?)\}\}/g
};

cw.underscorePartial = function (templateSelector, data) {
    return _.template($('#' + templateSelector).html())(data);
};

cw.checkForEnter = function (e) {
    if (e.which == 13 && !e.shiftKey) {
        e.preventDefault();
        $(e.target).blur();
    }
};

cw.materializeShit = function () {
    Materialize.updateTextFields();
    $('ul.tabs').tabs();
};
