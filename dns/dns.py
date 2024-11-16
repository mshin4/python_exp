import dns.resolver

with open("ARecords.txt") as a_records:
    records = list(a_records.readlines())

def check_a_record(records):
    for a_record in records:
        try:
            result = dns.resolver.resolve(a_record.strip("\n"), 'A')
            for ipval in result:
                print(a_record.strip("\n"), 'IP', ipval.to_text())

        except dns.resolver.NXDOMAIN:
            print(a_record.strip("\n"), "**This record does not exist.**")

check_a_record(records)
