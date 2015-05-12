import click
from click import ClickException
import json
from jinja2 import Environment, FileSystemLoader
import os.path


@click.command()
@click.option('--template-path', help='Path to template directory')
@click.option('--template', help='Jinja2 template')
@click.option('--tfstate', help='path to terraform state file')
@click.option('--inventory-output', help="file to save rendered template")
def compile_template(template_path, template, tfstate, inventory_output):
    """
    Takes a terraform state file and compiles a Jinja2 template

    example:\n
    terrible --template-path <path to templates>
    --template ansible-inventory.j2
    --tfstate terraform.tfstate
    --inventory-output inventory.ini
    """
    
    if template_path is None:
        raise ClickException("--template-path cannot be null")
    elif not os.path.isdir(template_path):
        raise ClickException("--template-path must be a directory")

    if template is None:
        raise ClickException("--template cannot be null")
    elif not os.path.isfile("%s/%s" % (template_path, template)):
        raise ClickException("--template file cannot be found")

    if tfstate is None:
        raise ClickException("--tfstate cannot be null")
    elif not os.path.isfile(tfstate):
        raise ClickException("--tfstate file cannot be found")

    if inventory_output is None:
        raise ClickException("--inventory-output must be specified")        

    
    tfstate_dict = parse_tfstate(tfstate)
    env = Environment(loader=FileSystemLoader(template_path))
    ansible_inventory_template = env.get_template(template)

    terraform_resources = tfstate_dict.get('modules').pop().get('resources')

    rendered = ansible_inventory_template.render(resources=terraform_resources)

    output_template = open(inventory_output, "w")
    output_template.write(rendered)
    output_template.close()


def parse_tfstate(tfsate_file_path):
    data_file = open(tfsate_file_path)
    return json.load(data_file)
