PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "rules_rule" (
    "id" serial NOT NULL PRIMARY KEY,
    "rule" text NOT NULL,
    "description" varchar(400) NOT NULL,
    "added" timestamp,
    "updated" timestamp
);
INSERT INTO "rules_rule" VALUES(1,'Kuvailu','Joku','2012-05-30 19:19:14.477831','2012-06-04 19:28:40.381884');
INSERT INTO "rules_rule" VALUES(2,'Kuvailu','Muu','2012-05-30 19:19:28.762605','2012-06-04 09:44:15.369812');
INSERT INTO "rules_rule" VALUES(3,'Honkolan kyläkirkko. "Tulkaa minun tyköni", ök, OA: J. Honkonen 1939. Puretun kyläkirkon entinen alttaritaulu. Kyläläiset antoivat taulun opettaja Toivo Parantaiselle (1921-1994), jonka jäämistö muuodostaa nykyään Liimattalan taidekodin kokoelman. Lähde: vierailu Liimattalassa 2001?, teoksesta otettu väripaperikuva.','Äänekoski','2012-06-03 19:04:54.734830','2012-06-09 13:29:17.869972');
COMMIT;