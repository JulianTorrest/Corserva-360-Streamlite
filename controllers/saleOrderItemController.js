const { SaleOrderItem } = require('../models');
const Joi = require('joi');

// Ejemplo de validación con Joi
const schema = Joi.object({
    productName: Joi.string().required(),
    quantity: Joi.number().integer().min(1).required(),
    price: Joi.number().positive().required()
});

module.exports = {
    create: async (req, res) => {
        try {
            const { error } = schema.validate(req.body);
            if (error) {
                return res.status(400).send(error.details[0].message);
            }

            const saleOrderItem = await SaleOrderItem.create(req.body);
            return res.json(saleOrderItem);
        } catch (err) {
            console.error(err);
            return res.status(500).send('Server Error');
        }
    },

    // Implementa las funciones restantes: read, update, delete
};
