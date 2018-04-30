import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_squid_is_installed(host):
    pkg = host.package('squid')
    assert pkg.is_installed


def test_squid_running_and_enabled(host):
    svc = host.service('squid')
    assert svc.is_running
    assert svc.is_enabled


def test_config_file(host):
    config_file = host.file('/etc/squid/squid.conf')
    assert config_file.is_file
    assert config_file.contains('http_port')


def test_output_file(host):
    output_file = host.file('/var/log/squid/squid.out')
    assert output_file.is_file
    assert output_file.contains('/var/spool/squid exists')
