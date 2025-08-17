# Parcial-2-Modulo-12---Prog4

🎯 Objetivo
Diseñar una API RESTful de solo lectura (GET-only) que permita consultar datos históricos sobre la vacunación contra el sarampión en niños de 12 a 23 meses en Panamá, utilizando la información provista por el Banco Mundial.

📝 Contexto
Se trabajará con el conjunto de datos del indicador SH.IMM.MEAS correspondiente a la cobertura de vacunación contra el sarampión en Panamá. El objetivo es construir una API pública que permita consultar estos datos de forma estructurada y reutilizable.

Fuente de datos:
🔗 Banco Mundial - SH.IMM.MEAS Panamá

📌 Requisitos funcionales
🔹 Endpoints requeridos
La API debe ser de solo lectura y exponer al menos los siguientes endpoints:

GET /vacunas
➤ Devuelve todos los registros disponibles.

GET /vacunas/<año>
➤ Devuelve el registro correspondiente al año especificado (ej. 2001).

GET /vacunas/provincia/<nombre> (opcional si los datos por región están disponibles)
➤ Devuelve los datos de vacunación para la provincia o región especificada.

En caso de que los datos del Banco Mundial no contengan detalles regionales, este endpoint puede simular datos regionales basados en el año.

💡 Consideraciones técnicas
La API debe estar implementada usando Flask, FastAPI o cualquier framework web en Python.

Los datos deben estar estructurados en formato JSON.

No se permiten métodos que modifiquen los datos (POST, PUT, DELETE).

El proyecto debe estar modularizado y bien documentado.

Agregar pruebas unitarias para al menos un endpoint (pytest, unittest, etc.).

🚀 Entrega
El proyecto debe subirse a un repositorio público o privado en GitHub o GitLab.

El enlace del repositorio debe compartirse en el espacio de entrega habilitado.
