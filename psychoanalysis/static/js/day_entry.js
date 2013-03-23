

var Activity = Backbone.Model.extend({
    defaults: {
        description: ''
    }
});


var Activities = Backbone.Collection.extend({
    model: Activity
});


var Category = Backbone.Model.extend({
    activities: null,

    initialize: function(options) {
        this.set('description', options['description']);
        this.activities = new Activities(options['activities']);
    },

    defaults: {
        description: ''
    }
});


var Categories = Backbone.Collection.extend({
    model: Category
});


$(document).ready(function() {

    var categories_data = [
        {
            description: 'Category 1',
            activities: [
                {
                    description: 'Activity 1',
                },
                {
                    description: 'Activity 2',
                },
                {
                    descritpion: 'Activity 3'
                }
            ]
        },
        {
            description: 'Category 2',
            activities: [
                {
                    description: 'Activity 4',
                },
                {
                    description: 'Activity 5',
                },
                {
                    descritpion: 'Activity 6'
                }
            ]
        }
    ];

    var categories = new Categories(categories_data);

});
