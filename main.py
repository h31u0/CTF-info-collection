from Producer import CtftimeProducer
from Consumer import SQLitreConsumer

def main():
	ctftime = CtftimeProducer()
	ctftime_res = ctftime.get_data()

	s = SQLitreConsumer("test.sql")
	s.create_connection()
	s.create_CTF_table()
	for i in ctftime_res:
		s.insert(list(i))
	s.close_connection()

if __name__ == "__main__":
    main()