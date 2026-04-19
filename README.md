# entregable-3-cicid

Staging ALB URL:    http://calculadora-staging-alb-248217973.us-east-1.elb.amazonaws.com/
Production ALB URL: http://calculadora-production-alb-935156225.us-east-1.elb.amazonaws.com/




1. Explica brevemente el flujo de trabajo nuevo completo que implementaste con Terraform (commit -> CI -> Build/Push Imagen -> Deploy TF Staging -> Update Service Staging -> Test Staging -> Deploy TF Prod -> Update Service Prod -> Smoke Test Prod). Sé específico sobre qué artefacto se mueve, qué hace cada job principal, y qué valida cada tipo de prueba.
2. ¿Qué ventajas y desventajas encontraste al usar Terraform o infraestructura como código en vez de desplegar manualmente? ¿Qué te pareció definir la infraestructura en HCL?
3. ¿Qué ventajas y desventajas tiene introducir un entorno de Staging en el pipeline de despliegue a AWS? ¿Cómo impacta esto la velocidad vs. la seguridad del despliegue?
4. ¿Qué diferencia hay entre las pruebas ejecutadas contra Staging (test-staging) y las ejecutadas contra Producción (smoke-test-production) en tu pipeline? ¿Por qué esta diferencia?
5. Considerando un ciclo completo de DevOps, ¿qué partes importantes (fases, herramientas, prácticas) crees que aún le faltan a este pipeline de CI/CD que has construido? (Menciona 2, explica por qué son importantes y cómo podrían implementarse brevemente).
6. 2¿Cómo te pareció implementar dos funcionalidades nuevas? ¿Qué tal fue tu experiencia? ¿Encontraste útil implementar CI/CD a la hora de realizar cambios y despliegues? ¿Por qué? ¿Qué no fue tan útil?
