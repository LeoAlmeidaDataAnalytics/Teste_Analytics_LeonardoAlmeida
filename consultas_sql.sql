'''
AQUI SAO CODIGOS SQL PARA CRIAÇÃO DE MINHAS TABELAS LOCAIS PARA REALIZAÇÃO DESSA CONSULTA

CREATE TABLE quod (
	id serial primary key,
	data DATE,
	produto varchar(50),
	categoria varchar(50),
	quantidade integer,
	preço integer
);
ALTER TABLE quod ALTER COLUMN preço TYPE numeric(10,2)


select * from quod

COPY quod(id, data, produto, categoria, quantidade, preço) FROM 'C:\testequod\data_clean.csv' DELIMITER ';' CSV HEADER;
'''


--ORDENANDO NOME DE PRODUTOS, CATEGORIA E A SOMA TOTAL DE VENDAS EM ORDEM DECRESCENTE
select produto, categoria, (quantidade * preço) as valor_total
from quod
order by valor_total DESC


--iDENTIFICANDO OS PRODUTOS QUE VENDERAM MENOS NO MES DE JUNHO DE 2023
select produto, (quantidade * preço) as valor_total, data
from quod
where data >= '2023-06-01' and data <= '2023-06-30'
GROUP BY produto, valor_total, data
order by valor_total ASC