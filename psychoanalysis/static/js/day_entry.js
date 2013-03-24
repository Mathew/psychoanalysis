

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


var ActivityEntries = Backbone.Collection.extend({
    model: ActivityEntry
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

        return this.$el;
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
                    activity_entry: this.model.toJSON(),
                    categories: this.categories.toJSON()
                }
            )
        );

        return this;

    }

});


var ActivityEntriesView = Backbone.View.extend({

    initialize: function(options) {
        this.categories = options['categories'];
    },

    render: function() {
        var that = this;

        this.collection.each(function(activity_entry) {
           view = new ActivityEntryView({model: activity_entry, categories: that.categories});
           that.$el.append(view.render().$el);
        });

        return this.$el;
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



    var activity_entries = new ActivityEntries([
        {day: 1, hour: 1, slot: 1, label: '0 - 15'},
        {day: 1, hour: 1, slot: 2, label: '15 - 30'},
        {day: 1, hour: 1, slot: 3, label: '30 - 45'},
        {day: 1, hour: 1, slot: 4, label: '45 - 60'}
    ]);

    var activity_entries_view = new ActivityEntriesView({el: '#activity_container', collection: activity_entries, categories: categories});
    activity_entries_view.render();

});
