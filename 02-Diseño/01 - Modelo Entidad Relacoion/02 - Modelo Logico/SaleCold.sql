CREATE DATABASE Salecold;
USE Salecold;

CREATE TABLE IF NOT EXISTS TipoDocumento (
  IdTipoDocumento INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_TipoDocumento PRIMARY KEY (IdTipoDocumento)
);

CREATE TABLE IF NOT EXISTS TipoUsuario (
  IdTipoUsuario INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_TipoUsuario PRIMARY KEY (IdTipoUsuario)
  );

CREATE TABLE IF NOT EXISTS Ciudad (
  IdCiudad INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CodigoPostal VARCHAR(45) NOT NULL,
  CONSTRAINT pk_Ciudad PRIMARY KEY (IdCiudad)

);

CREATE TABLE IF NOT EXISTS Usuario (
  IdUsuario INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(45) NOT NULL,
  Apellido VARCHAR(45) NOT NULL,
  NumeroDocumento VARCHAR(45) NOT NULL,
  Correo VARCHAR(45) NOT NULL UNIQUE,
  Contrasena VARCHAR(45) NOT NULL,
  Direccion VARCHAR(45) NOT NULL,
  TipoDocumento_IdTipoDocumento INT NOT NULL,
  TipoUsuario_IdTipoUsuario INT NOT NULL,
  Ciudad_IdCiudad INT NOT NULL,
  CONSTRAINT pk_Usuario PRIMARY KEY (IdUsuario),
  CONSTRAINT fk_Usuario_TipoDocumento1 FOREIGN KEY (TipoDocumento_IdTipoDocumento)
  REFERENCES TipoDocumento(IdTipoDocumento) ON DELETE RESTRICT  ON UPDATE CASCADE,
  CONSTRAINT fk_Usuario_TipoUsuario1 FOREIGN KEY (TipoUsuario_IdTipoUsuario)
  REFERENCES TipoUsuario(IdTipoUsuario) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_Usuario_Ciudad1 FOREIGN KEY (Ciudad_IdCiudad)
  REFERENCES Ciudad (IdCiudad) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS TipoDePago (
  IdTipoDePago INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_TipoPago PRIMARY KEY (IdTipoDePago)
);

CREATE TABLE IF NOT EXISTS TipoDeEntrega (
  IdTipoDeEntrega INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_TipoDeEntrega PRIMARY KEY (IdTipoDeEntrega)
);

CREATE TABLE IF NOT EXISTS ConfirmacionPedido (
  IdConfirmacionPedido INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_confirmacionPedido PRIMARY KEY (IdConfirmacionPedido)
  );

CREATE TABLE IF NOT EXISTS TipoDocumentoContable (
  IdTipoDocumentoContable INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  Naturaleza VARCHAR(45) NOT NULL,
  CONSTRAINT pk_TipoDocumento PRIMARY KEY (IdTipoDocumentoContable)
);

CREATE TABLE IF NOT EXISTS CabeceraPedido (
  IdCabeceraPedido INT AUTO_INCREMENT,
  FechaPedido VARCHAR(45) NOT NULL,
  FechaDePago VARCHAR(45) NOT NULL,
  NumeroDePago VARCHAR(45) NOT NULL,
  ReferenciaDePago VARCHAR(45) NOT NULL,
  Usuario_IdUsuario INT NOT NULL,
  ConfirmacionPedido_IdConfirmacionPedido INT NOT NULL,
  TipoDocumentoContable_IdTipoDocumentoContable INT NOT NULL,
  TipoDeEntrega_IdTipoDeEntrega INT NOT NULL,
  TipoDePago_IdTipoDePago INT NOT NULL,
  CONSTRAINT pk_CabeceraPedido PRIMARY KEY (IdCabeceraPedido),
  CONSTRAINT fk_Cabecera_Pedido_Usuario FOREIGN KEY (Usuario_IdUsuario) REFERENCES Usuario(IdUsuario)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE,
  CONSTRAINT fk_CabeceraPedido_ConfirmacionPedido FOREIGN KEY (ConfirmacionPedido_IdConfirmacionPedido) REFERENCES ConfirmacionPedido(IdConfirmacionPedido)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE ,
  CONSTRAINT fk_CabeceraPedido_TipoDocumentoContable FOREIGN KEY (TipoDocumentoContable_IdTipoDocumentoContable) REFERENCES TipoDocumentoContable(IdTipoDocumentoContable)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE ,
  CONSTRAINT fk_CabeceraPedido_TipodeEntrega FOREIGN KEY (TipoDeEntrega_IdTipoDeEntrega) REFERENCES TipoDeEntrega(IdTipoDeEntrega)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE,
	CONSTRAINT fk_CabeceraPedido_TipoDePago FOREIGN KEY (TipoDePago_IdTipoDePago) REFERENCES TipoDePago(IdTipoDePago)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Categorias (
  IdCategorias INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_Categorias PRIMARY KEY (IdCategorias)
);

CREATE TABLE IF NOT EXISTS UnidadDeMedida (
  IdUnidadDeMedida INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  CONSTRAINT pk_UnidadDeMedida PRIMARY KEY (IdUnidadDeMedida)
);

CREATE TABLE IF NOT EXISTS Producto (
  IdProducto INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  PrecioUnitario DECIMAL NOT NULL,
  Categorias_IdCategorias INT NOT NULL,
  UnidadDeMedida_IdUnidadDeMedida INT NOT NULL,
  CONSTRAINT pk_Producto PRIMARY KEY (IdProducto),
  CONSTRAINT fk_Producto_Categorias1 FOREIGN KEY (Categorias_IdCategorias) REFERENCES Categorias (IdCategorias)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE,
  CONSTRAINT fk_Producto_UnidadDeMedida1 FOREIGN KEY (UnidadDeMedida_IdUnidadDeMedida) REFERENCES UnidadDeMedida (IdUnidadDeMedida)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE 
);

CREATE TABLE IF NOT EXISTS DetallePedido (
  IdDetallePedido INT NOT NULL AUTO_INCREMENT,
  Cantidad VARCHAR(45) NOT NULL,
  Subtotal DECIMAL NOT NULL,
  Total DECIMAL NOT NULL,
  Producto_IdProducto INT NOT NULL,
  CabeceraPedido_IdCabeceraPedido INT NOT NULL,
  CONSTRAINT pk_DetallePedido PRIMARY KEY (IdDetallePedido),
  CONSTRAINT fk_Detalle_Pedido_Producto FOREIGN KEY (Producto_IdProducto) REFERENCES Producto(IdProducto)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE,
  CONSTRAINT fk_DetallePedido_CabeceraPedido FOREIGN KEY (CabeceraPedido_IdCabeceraPedido) REFERENCES CabeceraPedido(IdCabeceraPedido)
    ON DELETE RESTRICT 
	ON UPDATE CASCADE 
);

CREATE TABLE IF NOT EXISTS CabeceraDocumentoContable (
  IdCabeceraDocumentoContable INT NOT NULL AUTO_INCREMENT,
  NumeroDocumentoContable VARCHAR(45) NOT NULL,
  CabeceraPedido_IdCabeceraPedido INT NOT NULL,
  CONSTRAINT pk_CabeceraDocumentoContable PRIMARY KEY (IdCabeceraDocumentoContable),
  CONSTRAINT fk_CabeceraDocumentoContable_CabeceraPedido FOREIGN KEY (CabeceraPedido_IdCabeceraPedido) REFERENCES CabeceraPedido(IdCabeceraPedido)
   ON DELETE RESTRICT 
   ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS DetalleDocumentoContable (
  IdDetalleDocumentoContable INT NOT NULL,
  CabeceraDocumentoContable_IdCabeceraDocumentoContable INT NOT NULL,
  DetallePedido_IdDetallePedido INT NOT NULL,
  CONSTRAINT pk_DetalleDocumentoContable PRIMARY KEY (IdDetalleDocumentoContable),
  CONSTRAINT fk_DetalleDocumentoContable_CabeceraDocumentoContable FOREIGN KEY (CabeceraDocumentoContable_IdCabeceraDocumentoContable) REFERENCES CabeceraDocumentoContable(IdCabeceraDocumentoContable)
   ON DELETE RESTRICT 
   ON UPDATE CASCADE,
  CONSTRAINT fk_DetalleDocumentoContable_DetallePedido FOREIGN KEY (DetallePedido_IdDetallePedido) REFERENCES DetallePedido(IdDetallePedido)
   ON DELETE RESTRICT 
   ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Entregas (
  IdEntrega INT NOT NULL AUTO_INCREMENT,
  Descripcion VARCHAR(45) NOT NULL,
  DetalleDocumentoContable_IdDetalleDocumentoContable INT NOT NULL,
  CONSTRAINT pk_Entrega PRIMARY KEY (IdEntrega),
  CONSTRAINT fk_Entregas_DetalleDocumentoContable FOREIGN KEY (DetalleDocumentoContable_IdDetalleDocumentoContable)
    REFERENCES DetalleDocumentoContable (IdDetalleDocumentoContable)
   ON DELETE RESTRICT 
   ON UPDATE CASCADE
);

#Insertar y consultar datos de las entidades

SELECT * FROM TipoDocumento;
INSERT INTO TipoDocumento VALUES(1, 'Tarjeta de identidad');
INSERT INTO TipoDocumento VALUES(2, 'Cedula');
INSERT INTO TipoDocumento VALUES(3, 'Cedula de extranjeria');

SELECT * FROM TipoUsuario;
INSERT INTO TipoUsuario VALUES(1, 'Cliente');
INSERT INTO TipoUsuario VALUES(2, 'Administrador');
INSERT INTO TipoUsuario VALUES(3, 'Programador');

SELECT * FROM Ciudad;
INSERT INTO Ciudad VALUES (1, 'Bogota', 'B01');
INSERT INTO Ciudad VALUES (2, 'Cali', 'C01');
INSERT INTO Ciudad VALUES (3, 'Medellin', 'M01');

SELECT * FROM Usuario;
INSERT INTO Usuario VALUES (1, 'Daniel', 'Alfaro', '1234567', 'daniel@gmail.com', 'ggfdfs32', 'Calle 80 # 70 sur', 1, 1, 1);
INSERT INTO Usuario VALUES (2, 'Sara', 'Ortiz', '45667643', 'sara@gmail.com', 'dsahdsjbdas2', 'Calle 70 # 10 sur', 2, 2, 2);
INSERT INTO Usuario VALUES (3, 'Briam', 'Galindo', '87634321', 'briam@gmail.com', 'nj44224n*', 'Calle 40 # 20 sur', 3, 3, 3);

SELECT * FROM TipoDePago;
INSERT INTO TipoDePago VALUES (1, 'Efectivo');
INSERT INTO TipoDePago VALUES (2, 'Tarjeta');

SELECT * FROM TipoDeEntrega;
INSERT INTO TipoDeEntrega VALUES(1,'ContraEntrega');
INSERT INTO TipoDeEntrega VALUES(2,'Envio');
INSERT INTO TipoDeEntrega VALUES(3, 'Recoge en tienda');

SELECT * FROM ConfirmacionPedido;
INSERT INTO ConfirmacionPedido VALUES(1,'Confirmado');
INSERT INTO ConfirmacionPedido VALUES(2,'Pendiente de pago');

SELECT * FROM TipoDocumentoContable;
INSERT INTO TipoDocumentoContable VALUES (1, 'Primer','Debito');
INSERT INTO TipoDocumentoContable VALUES (2, 'Segundo','Credito');
INSERT INTO TipoDocumentoContable VALUES (3, 'Tercero','Debito');

SELECT * FROM CabeceraPedido;
INSERT INTO CabeceraPedido VALUES (1, '2021-02-01','2021-01-31', '2354jifdsd', '23545653', 1,1,1,1,1);
INSERT INTO CabeceraPedido VALUES (2, '2020-04-04','2020-04-06', 'dsbh33212', '455456323', 2,2,2,2,2);

SELECT * FROM Categorias;
INSERT INTO Categorias VALUES (1, 'Nueva');
INSERT INTO Categorias VALUES (2, 'Repuestos');
INSERT INTO Categorias VALUES (3, 'Ventiladores');

SELECT * FROM UnidadDeMedida;
INSERT INTO UnidadDeMedida VALUES (1, 'Kilo');
INSERT INTO UnidadDeMedida VALUES (2, 'Centimetro');
INSERT INTO UnidadDeMedida VALUES (3, 'Kilogramo');

SELECT * FROM Producto;
INSERT INTO Producto VALUES (1, 'Producto1', 1000, 1, 1);
INSERT INTO Producto VALUES (2, 'Producto2', 2000, 2, 2);
INSERT INTO Producto VALUES (3, 'Producto3', 3000, 3, 3);

SELECT * FROM DetallePedido;
INSERT INTO DetallePedido VALUES (1, 10, 1300, 1600, 1, 1);
INSERT INTO DetallePedido VALUES (2, 11, 2500, 3000, 2, 2);

SELECT * FROM CabeceraDocumentoContable;
INSERT INTO CabeceraDocumentoContable VALUES (1, 'DOC01', 1);
INSERT INTO CabeceraDocumentoContable VALUES (2, 'DOC02', 2);

SELECT * FROM DetalleDocumentoContable;
INSERT INTO DetalleDocumentoContable VALUES (1, 1, 1);
INSERT INTO DetalleDocumentoContable VALUES (2, 2, 2);

SELECT * FROM Entregas;
INSERT INTO Entregas VALUES (1, 'Entregado', 1);
INSERT INTO Entregas VALUES (2, 'Entregado', 2);

SELECT * FROM Usuario WHERE Correo = 'daniel@gmail.com';