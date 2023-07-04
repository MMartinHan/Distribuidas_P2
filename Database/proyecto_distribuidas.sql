/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     3/7/2023 12:20:59                            */
/*==============================================================*/


drop table if exists CANDIDATO;

drop table if exists COMPROBANTE;

drop table if exists CUENTA;

drop table if exists EMPLEADO;

drop table if exists EVALUACION;

drop table if exists MOTIVO;

drop table if exists NOMINA;

drop table if exists PARAMETROEVALUACION;

drop table if exists TIPO_CUENTA;

/*==============================================================*/
/* Table: CANDIDATO                                             */
/*==============================================================*/
create table CANDIDATO
(
   CEDULA_CAN           varchar(10) not null,
   NOMBRE_CAN           varchar(100) not null,
   APELLIDO_CAN         varchar(100) not null,
   FECHANACIMIENTO_CAN  date not null,
   primary key (CEDULA_CAN)
);

/*==============================================================*/
/* Table: COMPROBANTE                                           */
/*==============================================================*/
create table COMPROBANTE
(
   CODIGO_TC            varchar(8) not null,
   CODIGO_CUE           varchar(8) not null,
   CODIGO_COM           varchar(8) not null,
   FECHA_COM            date not null,
   OBSERVACIONES_COM    varchar(100) not null,
   CANTIDAD_DEBE_COM    decimal(8,2) not null,
   CANTIDAD_HABER_COM   numeric(8,2) not null,
   primary key (CODIGO_TC, CODIGO_CUE, CODIGO_COM)
);

/*==============================================================*/
/* Table: CUENTA                                                */
/*==============================================================*/
create table CUENTA
(
   CODIGO_TC            varchar(8) not null,
   CODIGO_CUE           varchar(8) not null,
   NOMBRE_CUE           varchar(50) not null,
   primary key (CODIGO_TC, CODIGO_CUE)
);

/*==============================================================*/
/* Table: EMPLEADO                                              */
/*==============================================================*/
create table EMPLEADO
(
   CODIGO_MOT           varchar(8) not null,
   CEDULA_EMP           varchar(10) not null,
   NOMBRE_EMP           varchar(35) not null,
   APELLIDO_EMP         varchar(35) not null,
   FECHA_ING_EMP        date not null,
   SUELDO_EMP           decimal(7,2) not null,
   primary key (CODIGO_MOT, CEDULA_EMP)
);

/*==============================================================*/
/* Table: EVALUACION                                            */
/*==============================================================*/
create table EVALUACION
(
   CEDULA_CAN           varchar(10) not null,
   CODIGO_PEV           varchar(100) not null,
   NUMERO_EVA           varchar(1000) not null,
   FECHA_EVA            date not null,
   CALIFICACION_EVA     decimal(5,2) not null,
   primary key (CEDULA_CAN, CODIGO_PEV, NUMERO_EVA)
);

/*==============================================================*/
/* Table: MOTIVO                                                */
/*==============================================================*/
create table MOTIVO
(
   CODIGO_MOT           varchar(8) not null,
   NOMBRE_MOT           varchar(10) not null,
   primary key (CODIGO_MOT)
);

/*==============================================================*/
/* Table: NOMINA                                                */
/*==============================================================*/
create table NOMINA
(
   CODIGO_MOT           varchar(8) not null,
   CEDULA_EMP           varchar(10) not null,
   CODIGO_NOM           varchar(8) not null,
   FECHA_NOM            date not null,
   DETALLE_NOM          varchar(500) not null,
   primary key (CODIGO_MOT, CEDULA_EMP, CODIGO_NOM)
);

/*==============================================================*/
/* Table: PARAMETROEVALUACION                                   */
/*==============================================================*/
create table PARAMETROEVALUACION
(
   CEDULA_CAN           varchar(10) not null,
   CODIGO_PEV           varchar(100) not null,
   NOMBRE_PEV           varchar(100) not null,
   PUNTAJEMAXIMO_PEV    decimal(5,2) not null,
   primary key (CEDULA_CAN, CODIGO_PEV)
);

/*==============================================================*/
/* Table: TIPO_CUENTA                                           */
/*==============================================================*/
create table TIPO_CUENTA
(
   CODIGO_TC            varchar(8) not null,
   NOMBRE_TC            varchar(50) not null,
   primary key (CODIGO_TC)
);

alter table COMPROBANTE add constraint FK_CUENTACOMPROBANTE foreign key (CODIGO_TC, CODIGO_CUE)
      references CUENTA (CODIGO_TC, CODIGO_CUE) on delete restrict on update restrict;

alter table CUENTA add constraint FK_TIPO_CUENTACUENTA foreign key (CODIGO_TC)
      references TIPO_CUENTA (CODIGO_TC) on delete restrict on update restrict;

alter table EMPLEADO add constraint FK_MOTIVOEMPLEADO foreign key (CODIGO_MOT)
      references MOTIVO (CODIGO_MOT) on delete restrict on update restrict;

alter table EVALUACION add constraint FK_PARAETROEVALUACION foreign key (CEDULA_CAN, CODIGO_PEV)
      references PARAMETROEVALUACION (CEDULA_CAN, CODIGO_PEV) on delete restrict on update restrict;

alter table NOMINA add constraint FK_EMPLEADONOMINA foreign key (CODIGO_MOT, CEDULA_EMP)
      references EMPLEADO (CODIGO_MOT, CEDULA_EMP) on delete restrict on update restrict;

alter table PARAMETROEVALUACION add constraint FK_CANDIDATOPARAMETRO foreign key (CEDULA_CAN)
      references CANDIDATO (CEDULA_CAN) on delete restrict on update restrict;

