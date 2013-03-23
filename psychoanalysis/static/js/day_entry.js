

var Activity = Backbone.Model.extend({
    defaults: {
        description: ''
    }
});


var Activities = Backbone.Collection.extend({
    model: Activity
});


var ActivityEntry = Backbone.Model.extend({
    defaults: {
        day: null,
        hour: null,
        slot: null,
        activity: null,
    }
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


var CategoriesView = Backbone.View.extend({

    render: function() {
        this.$el.html(
            _.template(
                $('#template-categories').html(),
                {categories: this.collection.toJSON()}
            )
        );
    }


});


var ActivityEntryView = Backbone.View.extend({

    initialize: function(options) {
        this.categories = options['categories'];
    },

    render: function() {

        this.$el.html(
            _.template(
                $('#template-activity-entry').html(),
                {
                    activity: this.model.toJSON(),
                    categories: this.categories.toJSON()
                }
            )
        );

    }

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
                    description: 'Activity 3'
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
                    description: 'Activity 6'
                }
            ]
        }
    ];

    var categories = new Categories(categories_data);

    var categories_view = new CategoriesView({el: '.categories', collection: categories});
    categories_view.render();


    var activity_entry_00 = new ActivityEntry({day: 1, hour: 1, slot: 1})
    var activity_entry_view = new ActivityEntryView({el: '#test', model: activity_entry_00, categories: categories});
    activity_entry_view.render();

});
