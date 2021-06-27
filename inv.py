x = '''
{
    "all": {
        "hosts": [],
        "children": [
            "lhft"
        ]
    },
    "bcp": {
        "hosts": [
            "lt-bcp1-pws13",
            "lt-bcp1-pws15"
        ]
    },
    "slurm": {
        "hosts": [
            "lt-hk1-asr03",
            "lt-hk1-rsr01",
            "lt-hk1-rsr04",
            "lt-tko1-rsr02",
            "lt-tko1-rsr03"
        ]
    },
    "mum2": {
        "hosts": [
            "lt-mum2-avm01"
        ],
        "children": [
            "mum2_prod",
            "mum2_uat",
            "mum2_admin"
        ]
    },
    "vm_prod": {
        "hosts": [
            "lt-mum1-pvm01",
            "lt-hk1-pvm01",
            "lt-hk1-pvm02",
            "lt-hkg1-pvm01",
            "lt-hkg1-avm04"
        ]
    },
    "hk1_admin": {
        "hosts": [
            "lt-hk1-asr03",
            "lt-hk1-avm01",
            "lt-hk1-avm02",
            "lt-hk1-avm07",
            "lt-hk1-avm08",
            "lt-hk1-avm09"
        ]
    },
    "hkg1_dev": {
        "hosts": [
            "lt-hkg1-dws01",
            "lt-hkg1-dws02",
            "lt-hkg1-dws03",
            "lt-hkg1-dws04",
            "lt-hkg1-dws05",
            "lt-hkg1-dws06",
            "lt-hkg1-dws07",
            "lt-hkg1-dws10",
            "lt-hkg1-dws12",
            "lt-hkg1-dws13",
            "lt-hkg1-dws14",
            "lt-hkg1-dws15",
            "lt-hkg1-dws16",
            "lt-hkg1-dws17",
            "lt-hkg1-dws18",
            "lt-hkg1-dws19",
            "lt-hkg1-dws28",
            "lt-hkg1-dws29"
        ]
    },
    "hkg1_uat": {
        "hosts": [
            "lt-hkg1-tsr01",
            "lt-hkg1-tsr02",
            "lt-hkg1-tsr03",
            "lt-hkg1-tsr04",
            "lt-hkg1-tsr05",
            "lt-hkg1-tsr06"
        ]
    },
    "hkg1_prod": {
        "hosts": [
            "lt-hkg1-pws03",
            "lt-hkg1-pws04",
            "lt-hkg1-pws11",
            "lt-hkg1-pws13",
            "lt-hkg1-pws14",
            "lt-hkg1-pws15",
            "lt-hkg1-pws16",
            "lt-hkg1-pws19",
            "lt-hkg1-pws20"
        ]
    },
    "mum1_prod": {
        "hosts": [
            "lt-mum1-psr01",
            "lt-mum1-psr02",
            "lt-mum1-psr03",
            "lt-mum1-psr04",
            "lt-mum1-psr05",
            "lt-mum1-psr06",
            "lt-mum1-psr11",
            "lt-mum1-psr12",
            "lt-mum1-psr13",
            "lt-mum1-psr15"
        ]
    },
    "mum2_prod": {
        "hosts": [
            "lt-mum2-psr01",
            "lt-mum2-psr02",
            "lt-mum2-psr03",
            "lt-mum2-psr04",
            "lt-mum2-psr05",
            "lt-mum2-psr06",
            "lt-mum2-pvm01"
        ]
    },
    "hkg1_admin": {
        "hosts": [
            "lt-hkg1-anb01",
            "lt-hkg1-asr03",
            "lt-hkg1-avm01",
            "lt-hkg1-aws02",
            "lt-hkg1-avm04"
        ]
    },
    "mum1_admin": {
        "hosts": [
            "lt-mum1-avm01",
            "lt-mum1-avm02"
        ]
    },
    "hk1_prod": {
        "hosts": [
            "lt-hk1-pvm01",
            "lt-hk1-pvm02",
            "lt-hkg1-pvm01"
        ]
    },
    "hk1": {
        "hosts": [],
        "children": [
            "hk1_admin",
            "hk1_test",
            "hk1_prod"
        ]
    },
    "mum1": {
        "hosts": [],
        "children": [
            "mum1_prod",
            "mum1_uat",
            "mum1_admin"
        ]
    },
    "lhft": {
        "hosts": [],
        "children": [
            "hk1",
            "hkg1",
            "mum2",
            "mum1",
            "vm_prod",
            "slurm"
        ]
    },
    "hkg1": {
        "hosts": [],
        "children": [
            "hkg1_prod",
            "hkg1_uat",
            "hkg1_admin",
            "hkg1_dev",
            "bcp"
        ]
    }
}
'''

print(x)
