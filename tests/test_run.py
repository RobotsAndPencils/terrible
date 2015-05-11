#!/usr/bin/env python
# -*- coding: utf-8 -*-

from preggy import expect
import click
from click.testing import CliRunner
from terrible.run import compile_template
from tests.base import TestCase

import os


class CompileTemplateTestCase(TestCase):

    def test_compile_template(self):
        base_dir = os.path.dirname(os.path.realpath(__file__)) + "/../"
        template_path = "%stests_resources/" % base_dir
        template = "ansible-inventory.j2"
        tfstate = "%stests_resources/terraform.tfstate" % base_dir
        inventory_output = "%stests_resources/test_output" % base_dir

        # Empty any previous test output
        open(inventory_output, 'w').close()
        runner = CliRunner()
        result = runner.invoke(compile_template, [
            '--template-path', template_path,
            '--template', template,
            '--tfstate', tfstate,
            '--inventory-output', inventory_output])

        expect(hasattr(runner, 'exception')).to_equal(False)
        expect(result.exit_code).to_equal(0)

        output = open(inventory_output).read()
        expect(output).to_include("1.2.3.4")


    def test_missing_required_params(self):
    	base_dir = os.path.dirname(os.path.realpath(__file__)) + "/../"
    	template_path = "%stests_resources/" % base_dir
        template = "ansible-inventory.j2"
        tfstate = "%stests_resources/terraform.tfstate" % base_dir
        inventory_output = "%stests_resources/test_output" % base_dir

        runner = CliRunner()
        # Missing --template-path arg
        result = runner.invoke(compile_template, [
        	'--template', template,
            '--tfstate', tfstate,
            '--inventory-output', inventory_output])

        expect(result.exit_code).to_be_greater_than(0)

        # Missing --template arg
        result = runner.invoke(compile_template, [
        	'--template-path', template_path,
            '--tfstate', tfstate,
            '--inventory-output', inventory_output])

        
        expect(result.exit_code).to_be_greater_than(0)

        # Missing --tfstate arg
        result = runner.invoke(compile_template, [
            '--template-path', template_path,
            '--template', template,
            '--inventory-output', inventory_output])
        expect(result.exit_code).to_be_greater_than(0)

        # Missing --inventory-output arg
        result = runner.invoke(compile_template, [
            '--template-path', template_path,
            '--template', template,
            '--tfstate', tfstate])
        expect(result.exit_code).to_be_greater_than(0)

        # Give a file instead of a directory for template path
        result = runner.invoke(compile_template, [
            '--template-path', tfstate])
        expect(result.exit_code).to_be_greater_than(0)

        # Give a path instead of an acutal template for --template
        result = runner.invoke(compile_template, [
            '--template-path', template_path,
            '--template', template_path])
        expect(result.exit_code).to_be_greater_than(0)

        # Give an inviald path for tfstate
        result = runner.invoke(compile_template, [
            '--template-path', template_path,
            '--template', template,
            '--tfstate', tfstate + "blahblahdoesnotexist",
            '--inventory-output', inventory_output])
        expect(result.exit_code).to_be_greater_than(0)





