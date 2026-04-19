# entregable-3-cicid

Staging ALB URL:    http://calculadora-staging-alb-248217973.us-east-1.elb.amazonaws.com/
Production ALB URL: http://calculadora-production-alb-935156225.us-east-1.elb.amazonaws.com/



1. Explica brevemente el flujo de trabajo nuevo completo que implementaste con Terraform (commit -> CI -> Build/Push Imagen -> Deploy TF Staging -> Update Service Staging -> Test Staging -> Deploy TF Prod -> Update Service Prod -> Smoke Test Prod). Sé específico sobre qué artefacto se mueve, qué hace cada job principal, y qué valida cada tipo de prueba.

 - **build-test-publish** Se encarga de la parte de CI, construye la aplicación, ejecuta linters, pruebas unitarias, análisis de Sonar y, si todo pasa, genera una imagen Docker etiquetada con el SHA del commit y la sube a Docker Hub. 
 
 - **deploy-tf-staging** Despliega la infraestructura en ECS para el entorno de staging usando Terraform, definiendo cluster, servicio, balanceador de carga, etc., e inyecta la URL de la imagen recién construida. 
 
 - **update-service-staging** fuerza un nuevo despliegue del servicio ECS para asegurar que se use la última imagen. 
 
 - **test-staging** Ejecuta pruebas de aceptación en Selenium contra la URL del ALB de staging, validando que la aplicación se comporta 
 correctamente en un entorno similar a producción.
 
 - **deploy-tf-prod** Despliega la misma infraestructura pero para producción, usando la misma imagen Docker. 
 
 - **update-service-prod** Fuerza el despliegue en producción.

 - **smoke-test-prod** Le hace las Smoke tests al ALB de producción para confirmar que el despliegue no rompió nada. Este flujo garantiza que la misma imagen probada en staging llegue a producción de manera automática y segura.

2. ¿Qué ventajas y desventajas encontraste al usar Terraform o infraestructura como código en vez de desplegar manualmente? ¿Qué te pareció definir la infraestructura en HCL?

- **Ventajas**: Terraform permite tener una infraestructura reproducible en cualquier entorno (Por ejemplo en diferentes nubes), elimina errores humanos y disminuyes los tiempos de los despliegues. 

- **Desventaja**: Una curva de aprendizaje bastante importante, especialmente al depurar errores de sintaxis HCL o entender los recursos de AWS. 

Definir la infraestructura en HCL es bastante claro y presenta muchas ventajas con respecto a hacerlo todo manualmente,sin embargo, la documentación de los recursos es un poco confusa, esto aumenta la curva de aprenizaje necesaria para usar esta herramienta. 

3. ¿Qué ventajas y desventajas tiene introducir un entorno de Staging en el pipeline de despliegue a AWS? ¿Cómo impacta esto la velocidad vs. la seguridad del despliegue?

La principal ventaja es que staging actúa como un entorno de preproducción donde se pueden ejecutar pruebas de aceptación sin afectar usuarios reales. Esto aumenta la seguridad del despliegue, ya que se detectan problemas antes de llegar a producción. La desventaja es que añade tiempo al pipeline, lo que reduce la velocidad de entrega. Sin embargo, el trade-off vale la pena porque previene errores en producción y permite validar la integración con servicios AWS reales.

4. ¿Qué diferencia hay entre las pruebas ejecutadas contra Staging (test-staging) y las ejecutadas contra Producción (smoke-test-production) en tu pipeline? ¿Por qué esta diferencia?

En staging se ejecutan pruebas de aceptación completas, que simulan interacciones de usuario complejas y requieren tiempo. En producción solo se ejecutan smoke tests, que verifican rápidamente que la aplicación esté respondiendo, cargue la página y muestre el título correcto.  Las pruebas de aceptación son exhaustivas y podrían afectar el rendimiento de producción si se ejecutan frecuentemente, en producción se prioriza la disponibilidad y la detección temprana de fallos graves, mientras que la validación funcional ya se hizo en staging. Así, se balancea confianza y velocidad.

5. Considerando un ciclo completo de DevOps, ¿qué partes importantes (fases, herramientas, prácticas) crees que aún le faltan a este pipeline de CI/CD que has construido? (Menciona 2, explica por qué son importantes y cómo podrían implementarse brevemente).

- **Monitoreo y observabilidad en producción**: una vez desplegada la aplicación, es crucial monitorizar métricas (latencia, errores, uso de CPU) y logs centralizados para detectar problemas proactivamente. Podría implementarse con AWS CloudWatch Dashboards y alarmas, o herramientas como Prometheus/Grafana integradas en el contenedor. 
- **Rollback automático**: si las pruebas de humo fallan, el pipeline debería revertir automáticamente a la versión anterior. Esto se puede lograr con un job adicional que capture el fallo y ejecute terraform apply con la imagen anterior.

6. ¿Cómo te pareció implementar dos funcionalidades nuevas? ¿Qué tal fue tu experiencia? ¿Encontraste útil implementar CI/CD a la hora de realizar cambios y despliegues? ¿Por qué? ¿Qué no fue tan útil?

Implementar estas funciones nos permitió  ver el ciclo completo de CI/CD: añadir una funcionalidad, escribir pruebas unitarias y de aceptación, y ver cómo el pipeline las valida y despliega automáticamente. La experiencia fue satisfactoria, ya que el CI/CD nos dio confianza de que los cambios no rompían lo existente. Fue muy útil porque automatiza la validación y el despliegue, ahorrando tiempo manual y reduciendo errores.