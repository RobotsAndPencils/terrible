# Terrible
A command line tool for transforming [terraform](https://terraform.io/) state into [ansible](http://docs.ansible.com/) inventory files

Terraform is great at deploying infrastructure. This project aims to make using ansible and terraform together easy.

### Installing

    pip install git+git://github.com/RobotsAndPencils/terrible

### Using
Write your terraform config as you usually would

    # app.tf
    resource "aws_instance" "app-server" {
        ami = "aminumber"
        instance_type = "t2.small"
        key_name = "keyname"
        count = 1
        tags {
            Name = "server"
        }

        connection {
            user = "ubuntu"
            key_file = "key_path"
        }
    }

Create a [Jinja2](http://jinja.pocoo.org/) template for your ansible [inventory file](http://docs.ansible.com/intro_inventory.html)

    # ansible-inventory.j2
    # Inventory for provisioning app-server
    #
    {% for resource in resources %}
    {% for key, value in resource.iteritems() -%}
    {% if "aws_instance.app-server" in key %}

    [app-server]
    # you can reference any terraform attribute
    # https://www.terraform.io/docs/providers/aws/r/instance.html
    {{ value.primary.attributes.public_ip }} ansible_ssh_user=ubuntu

    {%- endif %}
    {%- endfor %}
    {%- endfor %}

Run terraform normally, then use terrible to convert terraform state to ansible inventory

    terraform plan
    terraform apply

    terrible --template-path $PWD \
    --template ansible-inventory.j2 \
    --tfstate terraform.tfstate \
    --inventory-output inventory.ini \

Now you can do normal ansible commands

    ansible app-server -m ping --inventory-file=inventory.ini

### Contributing

    git clone git@github.com:RobotsAndPencils/terrible.git

You may want to set up a [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) by running `virtualenv .venv; source .venv/bin/activate` before you use the make file.

    make setup
    make test

### Contact

[![Robots & Pencils Logo](http://f.cl.ly/items/2W3n1r2R0j2p2b3n3j3c/rnplogo.png)](http://www.robotsandpencils.com)

Made with :heart: by Robots & Pencils ([@robotsNpencils](https://twitter.com/robotsNpencils))

#### Maintainers

- [Curtis Allen](http://github.com/curtisallen) ([@cnallen](https://twitter.com/cnallen))
