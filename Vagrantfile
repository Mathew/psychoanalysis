Vagrant::Config.run do |config|

  config.vm.box = "lucid32"
  config.vm.box_url = "http://files.vagrantup.com/lucid32.box"

  config.vm.network :hostonly, "33.33.33.10"
  config.vm.forward_port 8000, 8000

  config.vm.customize ["modifyvm", :id, "--rtcuseutc", "on"]
  config.vm.provision :chef_solo do |chef|

  #chef.recipe_url = "http://cloud.github.com/downloads/Mathew/chef_recipes/cookbooks.tar.gz"
  #chef.cookbooks_path = [:vm, "cookbooks"]
  chef.cookbooks_path = ["cookbooks"]

    chef.add_recipe "main"
    chef.add_recipe "python"
    chef.add_recipe "postgres"

    chef.json.merge!({

      :project_name => "psychoanalysis",

      :user_name => "vagrant",
      :user_group => "vagrant",
      :dev_env => true,
      :postgres_password => "postgres",
      :project_db_user => "psychoanalysis",
      :project_db_pass => "psychoanalysis",
      :project_db_name => "psychoanalysis",
      :supervisor_user => "supervisor",
      :supervisor_password => "password",

      :system_packages => ['libjpeg62-dev'],
      :python_global_packages => [],
      :python_packages => [],

    })

  end

end

