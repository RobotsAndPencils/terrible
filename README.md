# Terrible
A command line tool for transforming [terraform](https://terraform.io/) state into [ansible](http://docs.ansible.com/) inventory files

### Installing

    pip install git+git://github.com/RobotsAndPencils/terrible

### Using
    terrible --template-path <path to templates> \
    --template ansible-inventory.j2 \
    --tfstate terraform.tfstate \ 
    --inventory-output inventory.ini \
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