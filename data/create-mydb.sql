# Excluir a base de dados
drop database Jobs;

# Cria a base de dados
create database Jobs;

# Mostrar as bases de dados
# show databases;

# Acessar o database
use Jobs;

# Excluindo tabelas
# drop table company;

# Criando as tabelas do banco
create table job(
	id_job int not null auto_increment,
    job_title varchar(255) not null,
    salary varchar(255),
    date varchar(255),
    id_company int not null,
    
    unique (id_job, id_company),
    primary key (id_job)    
);

create table company(
	id_company int not null auto_increment,
    company_name varchar(255) not null,
    # location varchar(255) not null,
    logo varchar(255),
    job_link varchar(2000),
    company_rating decimal(10, 2),
    id_job int not null,
    id_location int not null,
    
    unique (id_company, id_job, id_location),
    primary key(id_company)    
);

create table location(
	id_location int not null auto_increment,
    location varchar(255) not null,
    # id_company int not null,
    
    # unique (id_location, id_company),
    unique (id_location),
    primary key(id_location)
);

# carregando csv

# habilita o carregamento de arquivos (executar caso necessario)
# show global variables like 'local_infile';
# set global local_infile=true;
# select @@GLOBAL.secure_file_priv;

# job
# load data local infile "C:/temp/job.csv"
load data infile "c:/temp/api-data-science-job-salaries/data/job.csv"
into table job
fields terminated by ','
lines terminated by '\n';
# ignore 1 lines;

# company
load data infile "c:/temp/api-data-science-job-salaries/data/company.csv"
into table company
fields terminated by ','
lines terminated by '\n';

# location
load data infile "c:/temp/api-data-science-job-salaries/data/location.csv"
into table location
fields terminated by ','
lines terminated by '\n';

# Criando relacionamento entre as tabelas

# job
alter table job
add constraint fk_job_id_company
foreign key (id_company) references company(id_company);

# company
alter table company
add constraint fk_company_id_job
foreign key (id_job) references job(id_job);

alter table company
add constraint fk_company_id_location
foreign key (id_location) references location(id_location);

# visializando informações

# criar view all jobs
create view vw_jobs as
select 
company.id_company as "ID", 
company.company_name as "Empresa", 
location.location as "Localizacao",
job.job_title as "Emprego"
from company
inner join location
on company.id_location = location.id_location
inner join job
on company.id_job = job.id_job;
# where company.id_company = 1;

# visualizar view jobs
select * from vw_jobs;



