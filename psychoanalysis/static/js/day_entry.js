

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
