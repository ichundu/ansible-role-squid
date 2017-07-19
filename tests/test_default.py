import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_squid_is_installed(Package):
    squid = Package("squid")
    assert squid.is_installed


def test_squid_running_and_enabled(Service):
    squid = Service("squid")
    assert squid.is_running
    assert squid.is_enabled


def test_config_file(File):
    config_file = File('/etc/squid/squid.conf')
    assert config_file.is_file
    assert config_file.contains('http_port 3128')


def test_output_file(File):
    output_file = File('/var/log/squid/squid.out')
    assert output_file.is_file
    assert output_file.contains('/var/spool/squid exists')
