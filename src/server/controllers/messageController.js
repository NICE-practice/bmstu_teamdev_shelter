const { Message } = require("../models/modelsORM");
const ApiError = require("../errors/ApiError");
const MessageDTO = require("../models/messageDTO");

class MessageController {
  async add(req, res, next) {
    const {
      messageName,
      phone,
      email,
      messageText,
      preferredContactMethod,
      answerFlag,
      messageId,
    } = req.body;

    try {
      const messageORM = await Message.create({
        messageId,
        messageName,
        phone,
        email,
        messageText,
        preferredContactMethod,
        answerFlag,
      });

      const messageDTO = new MessageDTO(messageORM);
      return res.json(messageDTO);
    } catch (err) {
      return next(ApiError.internal(err.message));
    }
  }

  async getList(req, res) {
    let { limit, page } = req.query;

    page = page || 1;
    limit = limit || 9;
    const offset = page * limit - limit;

    const { count, rows } = await Message.findAndCountAll({ limit, offset });
    const messagesCount = count;
    const messagesORM = rows;
    const messagesDTO = [];
    for (const messageORM of messagesORM) {
      const messageDTO = new MessageDTO(messageORM);
      messagesDTO.push(messageDTO);
    }
    return res.json({ messages: messagesDTO, messagesCount });
  }

  async getById(req, res, next) {
    const { messageId } = req.params;

    const messageORM = await Message.findByPk(messageId);
    if (!messageORM) {
      return next(
        ApiError.badRequest(
          `Message with messageId=${messageId} does not exist`
        )
      );
    }

    try {
      const messageDTO = new MessageDTO(messageORM);
      return res.json(messageDTO);
    } catch (err) {
      return next(ApiError.internal(err.message));
    }
  }

  async changeAnswerFlagById(req, res, next) {
    const { messageId } = req.params;
    const { answerFlag } = req.body;

    const messageORM = await Message.findByPk(messageId);
    if (messageORM) {
      messageORM.update({ answerFlag });
      const messageDTO = new MessageDTO(messageORM);
      return res.json(messageDTO);
    }

    return next(
      ApiError.badRequest(`Message with messageId=${messageId} does not exist`)
    );
  }
}

module.exports = new MessageController();
