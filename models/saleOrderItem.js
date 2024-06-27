module.exports = (sequelize, DataTypes) => {
    const SaleOrderItem = sequelize.define('SaleOrderItem', {
        productName: {
            type: DataTypes.STRING,
            allowNull: false
        },
        quantity: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        price: {
            type: DataTypes.FLOAT,
            allowNull: false
        }
    });

    return SaleOrderItem;
};
